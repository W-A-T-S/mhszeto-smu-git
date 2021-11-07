$('#tfqns').on('change', function () {
    var value = $(this).val();
    var output = '';
    for (var i = 0; i <= value - 1; i++) {
       output += '<div>' +

          '<label>Question ID</label>' +
          '<input type="text" class="form-control question_id_tf" name="qn_id"' + i + ' required>' +
          '<label>Question</label>' +
          '<input type="text" class="form-control question_tf" name="quiz_qn"' + i + 'required>' +
          '<label>Correct Answer</label>' +
          `<input class="form-check-input correct_ans_tf" type="radio" name="correct_ans_tf${i}" id="truebtn"' + i + '>` +
          '<label class="form-check-label" for="correct_ans"> True</label>' +
          `<input class="form-check-input correct_ans_tf" type="radio" name="correct_ans_tf${i}" id="falsebtn"' + i + '>` +
          '<label class="form-check-label" for="correct_ans"> False </label>' +
          '</div><br><br>'
    }
    $('#tfquestionform').empty().append(output);
 });


 $('#mcqqns').on('change', function () {
    var value = $(this).val();
    var output = '';
    for (var j = 0; j <= value - 1; j++) {
       output += '<div>' +

          ' <br><label>Question ID</label>' +
          '<input type="text" class="form-control question_id_mcq" name="question_id" required>' +
          '<label>Question</label>' +
          '<input type="text"  class="form-control question_mcq" name="quiz_qn" required>' +
          '<label>Correct Answer</label>' +
          '<input type="text" class="form-control" name="correct_ans_mcq" required>' +
          '<label>Question Option(s)</label>' +
          '<input type="text" class="form-control qn_options" name="qn_options" required>' +
          '</div><br><br>'

    }
    $('#mcqquestionform').empty().append(output);
 });






 function create_quiz() {
    const course_id = document.getElementById("course_id").value;
    const class_id = document.getElementById("class_id").value;
    const lesson_id = document.getElementById("lesson_id").value;
    const description = document.getElementById("description").value;
    const time_limit = document.getElementById("time_limit").value;
    const pass_percent = document.getElementById("pass_percent").value;
    const is_final_true = document.getElementsByName("is_final")[0];
    const is_final_false = document.getElementsByName("is_final")[1];
    let is_final;
    if (is_final_true.checked) {
       is_final = true
    } else {
       is_final = false
    }

    const title = document.getElementById("title").value;
    console.log("This is is_final", is_final)
    const questions = []
    const num_of_qns = document.getElementsByClassName("question_id_tf").length;
    for (var x = 0; x < num_of_qns; x++) {
       const question_id = document.getElementsByClassName("question_id_tf")[x].value;
       const question = document.getElementsByClassName("question_tf")[x].value;
       const correct_answer_true = document.getElementsByName(`correct_ans_tf${x}`)[0];
       const correct_answer_false = document.getElementsByName(`correct_ans_tf${x}`)[1];

       let correct_answer;
       if (correct_answer_true.checked) {
          correct_answer = 1
       } else {
          correct_answer = 2
       }
       questions.push({
          lesson_id: lesson_id,
          class_id: class_id,
          course_id: course_id,
          question_id: question_id,
          question: question,
          options: [true, false],
          answer: correct_answer
       })
    }

    const num_of_qns_mcq = document.getElementsByClassName("question_id_mcq").length;
    for (var x = 0; x < num_of_qns_mcq; x++) {
       const question_id = document.getElementsByClassName("question_id_mcq")[x].value;
       const question = document.getElementsByClassName("question_mcq")[x].value;
       const correct_answer = document.getElementsByName("correct_ans_mcq")[x].value;
       const qn_options = document.getElementsByClassName("qn_options")[x].value.split(",");

       questions.push({
          lesson_id: lesson_id,
          class_id: class_id,
          course_id: course_id,
          question_id: question_id,
          question: question,
          options: qn_options,
          answer: correct_answer
       })
    }

    const data = {
       "course_id": course_id,
       "class_id": class_id,
       "lesson_id": lesson_id,
       "description": description,
       "time_limit": time_limit,
       "passing_percentage": pass_percent,
       "is_final": is_final,
       "questions": questions,
       "title": title
    };
    console.log(data)

    // document
    // console.log(cou)
    const response = fetch("/create_quiz", {
       method: 'POST',
       headers: {
          'Content-Type': 'application/json'
       },
       body: JSON.stringify(data)
    });
 }
