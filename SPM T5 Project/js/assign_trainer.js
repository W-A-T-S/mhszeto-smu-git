

fetch('http://127.0.0.1:5001/assign_trainer/json/CR102/CL2')
  .then(response => response.json())
  .then((raw) => {
      document.getElementById("class_id").innerText=raw.data.class.id;
      document.getElementById("course_id").innerText=`${raw.data.course.id} - ${raw.data.course.title}`;
      document.getElementById("class_start_date_time").innerText=raw.data.class.start_date_time;
      document.getElementById("class_end_date_time").innerText=raw.data.class.end_date_time;
      document.getElementById("trainer_name_username").value=`${raw.data.class.trainer_name} - ${raw.data.class.trainer_username}`

      console.log(raw.data.trainers);
  
      trainers_list="";
      for(let trainer of raw.data.trainers){
            trainers_list=trainers_list+`  
            <tr>
                <td>${trainer.username}</td>
                <td>${trainer.name}</td>
                <td>${trainer.current_designation}</td>
                <td>${trainer.num_classes_running}</td>
                <td>${trainer.num_classes_assigned}</td>
                <td> 
                    <button type="button" class="btn btn-info" onclick="select_trainer('${trainer.username}','${trainer.name}' )" on>Select</button></td>
                </td>
            </tr>`
      }

      document.getElementById("trainers-list").innerHTML= trainers_list
      
  });


function select_trainer(trainer_username,trainer_name){
    document.getElementById("trainer_name_username").value=`${trainer_name} - ${trainer_username}`  
    $('#assignTrainerModal').modal('hide');
    document.getElementById("insert-alert-div").innerHTML=''
}

function confirm_assign_trainer(){
    $('#confirmation-modal').modal('show');
    const class_id= document.getElementById("class_id").innerText;
    const course_id= document.getElementById("course_id").innerText.split(" - ")[0];
    const trainer_name= document.getElementById("trainer_name_username").value.split(" - ")[0];
    const trainer_username= document.getElementById("trainer_name_username").value.split(" - ")[1];
    document.getElementById("confirmation-modal-body").innerHTML=`You are about to assign <b>${trainer_name}(${trainer_username})</b> to class <b>${class_id}</b> of course <b>${course_id}</b>`
}

function assign_trainer(){
    const class_id= document.getElementById("class_id").innerText;
    const course_id= document.getElementById("course_id").innerText.split(" - ")[0];
    const trainer_name= document.getElementById("trainer_name_username").value.split(" - ")[0];
    const trainer_username= document.getElementById("trainer_name_username").value.split(" - ")[1];
    console.log(trainer_name)
    console.log(trainer_username)
    let response = fetch(`http://127.0.0.1:5001/assign_trainer/json/${course_id}/${class_id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify({trainer_name,trainer_username})
      });
    
    $('#confirmation-modal').modal('hide');
    document.getElementById("insert-alert-div").innerHTML=`
        <div class=" container alert alert-warning alert-dismissible fade show" id="success-alert" role="alert">
            Successfully assigned trainer!
            <button class="btn" data-bs-dismiss="alert" aria-label="Close">
                <span aria-hidden="true">&times;</span>
            </button>
        </div`
}