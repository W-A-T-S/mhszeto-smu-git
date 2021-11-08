var currentquestion = 0;
var correctAnswers = 0;
function checkAns() {
var selectedans = document.querySelector('input[name="option"]:checked').value;

  if (Number(selectedans) + 1 == allQuestions[currentquestion].correctAnswer) {
    correctAnswers++;
  };
}
function setupOptions() {

  $('#question').html(allQuestions[currentquestion].question);
  var options = allQuestions[currentquestion].choices;
  var formHtml = '';
  for (var i = 0; i < options.length; i++) {
    formHtml += '<div><input type="radio" name="option" value="' + i + '" id="option' + i + '"><label for="option' + i + '">' + allQuestions[currentquestion].choices[i] + '<br/></label><br/></div>';
  }
  $('#form').html(formHtml);
}

$(document).ready(function () {

  $("#container").hide();
  $('#start').click(function () {
    $("#container").fadeIn();
    $(this).hide();
    countdown();
  });



  setupOptions();

  $("#next").click(function () {
    checkAns();
    currentquestion++;


    if (currentquestion < allQuestions.length) {
      setupOptions();
      if (currentquestion == allQuestions.length - 1) {

        $('#next').html("Submit");
        
        $('#next').click(function () {
          $("#container").hide();
          var marks = correctAnswers * 100 / (allQuestions.length);
          clearInterval(myTimer);
          if (marks >= Number(quiz.passing_percentage)) {
            if (quiz.is_final) {
              $("#result").html("<p style='color:green;'>Your Score is " + correctAnswers + " out of " + allQuestions.length + " and your percentage is " + (marks) + "%" + "You have pass the final quiz. Congrats on completing the course.</p>").hide();
            } else {
              $("#result").html("<p style='color:green;'>Your Score is " + correctAnswers + " out of " + allQuestions.length + " and your percentage is " + (marks) + "%" + "Congrats on completing the lesson.</p>").hide();
            }
          } else {
            $("#result").html("<p style='color:red;'>Your Score is " + correctAnswers + " out of " + allQuestions.length + " and your percentage is " + (marks) + "%" + " You have failed the final quiz, please retake the quiz.</p>").hide();
          }

          $("#result").fadeIn(1500);
          var data = {
            "quiz_attempt_id": `QA ${Math.floor(Math.random() * (1000 - 10 + 1) + 10)}`, "lesson_id": quiz.lesson_id, "learner_username": "JohnSmithTheMan", "course_id": quiz.course_id, "class_id": quiz.class_id, "marks_awarded": marks, "is_passed": (marks >= Number(quiz.passing_percentage))
          }


          fetch('/update_attempt', {
            method: 'POST', // or 'PUT'
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
          })
            .then(response => {
              if (quiz.is_final) {
                location.replace("http://18.234.140.174:5007/view_completed_courses/JohnSmithTheMan");
              } else {
                location.replace("http://18.234.140.174:5009/view_lesson/CL1/CR101/JohnSmithTheMan");
              }
            })
            .catch((error) => {
              console.error('Error:', error);
            });
        });

      }

    };
  });
});

function submit_ans() {

  $("#container").hide();

  var marks = correctAnswers * 100 / (allQuestions.length);
  clearInterval(myTimer);
  if (marks >= Number(quiz.passing_percentage)) {
    if (quiz.is_final) {
      $("#result").html("<p style='color:green;'>Your Score is " + correctAnswers + " out of " + allQuestions.length + " and your percentage is " + (marks) + "%" + " You have pass the final quiz. Congrats on completing the course.</p>").hide();
    } else {
      $("#result").html("<p style='color:green;'>Your Score is " + correctAnswers + " out of " + allQuestions.length + " and your percentage is " + (marks) + "%" + " You have pass the quiz. Congrats on completing the lesson.</p>").hide();
    }
  } else {
    $("#result").html("<p style='color:red;'>Your Score is " + correctAnswers + " out of " + allQuestions.length + " and your percentage is " + (marks) + "%" + " You have failed the final quiz, please retake the quiz.</p>").hide();
  }
  $("#result").fadeIn(1500);

}
var myTime;
function countdown() {
  var count1 = Number(quiz.time_limit) * 60;
  myTimer = setInterval(function () {
    document.getElementById("timer").innerHTML = `${Math.round(count1 / 60) - 1} Minutes ${count1 % 60} Seconds`;
    count1--;
    console.log(count1)
    if (count1 == 0) {
      clearInterval(myTimer);
      submit_ans();
    }
  }, 1000);
}