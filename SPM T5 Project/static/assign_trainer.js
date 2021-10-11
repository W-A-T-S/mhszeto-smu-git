function initial_fetch() {
	fetch(`http://127.0.0.1:5001/assign_trainer/json/${course_id}/${class_id}`)
		.then((response) => response.json())
		.then((raw) => {
			document.getElementById('class_id').innerText = raw.data.class.id;
			document.getElementById(
				'course_id'
			).innerText = `${raw.data.course.id} - ${raw.data.course.title}`;
			document.getElementById('class_start_date_time').innerText = new Date(raw.data.class.start_date_time);
			document.getElementById('class_end_date_time').innerText =new Date(raw.data.class.end_date_time);

			if (raw.data.class.trainer_name && raw.data.class.trainer_username) {
				document.getElementById(
					'trainer_name_username'
				).value = `${raw.data.class.trainer_name} - ${raw.data.class.trainer_username}`;
			}

			trainers_list = '';
			for (let trainer of raw.data.trainers) {
				let select_btn = ``;
				if (trainer.username == raw.data.class.trainer_username) {
					select_btn = ` <button type="button" id="${trainer.username}" class="btn btn-secondary" onclick="select_trainer('${trainer.username}','${trainer.name}' )" disabled>Selected</button>`;
				} else {
					select_btn = `<button type="button" id="${trainer.username}" class="btn btn-info" onclick="select_trainer('${trainer.username}','${trainer.name}' )">Select</button></td>`;
				}

				trainers_list =
					trainers_list +
					`  
              <tr>
                  <td>${trainer.username}</td>
                  <td>${trainer.name}</td>
                  <td>${trainer.current_designation}</td>
                  <td>${trainer.num_classes_running}</td>
                  <td>${trainer.num_classes_assigned}</td>
                  <td>${select_btn}</td>
              </tr>`;
			}
			document.getElementById('trainers-list').innerHTML = trainers_list;
		})
		.catch(() => {
			document.getElementById('insert-alert-div').innerHTML = `
        <div class=" container alert alert-danger alert-dismissible fade show" id="success-alert" role="alert">
            Invalid class or course id!
            <button class="btn" data-bs-dismiss="alert" aria-label="Close">
                <span aria-hidden="true">&times;</span>
            </button>
        </div`;
		});

}

initial_fetch();

function select_trainer(cur_trainer_username, cur_trainer_name) {
	const prev_trainer_username = document
		.getElementById('trainer_name_username')
		.value.split(' - ')[1];
	document.getElementById('insert-alert-div').innerHTML = '';
	document.getElementById(
		'trainer_name_username'
	).value = `${cur_trainer_name} - ${cur_trainer_username}`;
	$('#assignTrainerModal').modal('hide');
	unselect_select_trainer(prev_trainer_username, cur_trainer_username);
}

function unselect_select_trainer(prev_trainer_username, cur_trainer_username) {
	if (prev_trainer_username) {
		prev_trainer_btn = document.getElementById(prev_trainer_username);
		prev_trainer_btn.removeAttribute('disabled');
		prev_trainer_btn.setAttribute('class', 'btn btn-info');
		prev_trainer_btn.innerText = 'Select';
	}

	const cur_trainer_btn = document.getElementById(cur_trainer_username);
	cur_trainer_btn.disabled = true;
	cur_trainer_btn.setAttribute('class', 'btn btn-secondary');
	cur_trainer_btn.innerText = 'Selected';
}

function confirm_assign_trainer() {
	const trainer_name = document
		.getElementById('trainer_name_username')
		.value.split(' - ')[0];
	const trainer_username = document
		.getElementById('trainer_name_username')
		.value.split(' - ')[1];
	document.getElementById(
		'confirmation-modal-body'
	).innerHTML = `You are about to assign <b>${trainer_name}(${trainer_username})</b> to class <b>${class_id}</b> of course <b>${course_id}</b>`;
	$('#confirmation-modal').modal('show');
}

function assign_trainer() {
	const trainer_name = document
		.getElementById('trainer_name_username')
		.value.split(' - ')[0];
	const trainer_username = document
		.getElementById('trainer_name_username')
		.value.split(' - ')[1];

	fetch(`http://127.0.0.1:5001/assign_trainer/json/${course_id}/${class_id}`, {
	// fetch(`http://127.0.0.1:5001/assign_trainer/json/123/123`, {
		method: 'PUT',
		headers: {
			'Content-Type': 'application/json;charset=utf-8',
		},
		body: JSON.stringify({ trainer_name, trainer_username }),
	})
		.then((response) => response.json())
		.then((raw) => {
			$('#confirmation-modal').modal('hide');
			if (raw.code == 200) {
				document.getElementById('insert-alert-div').innerHTML = `
            <div class=" container alert alert-warning alert-dismissible fade show" id="success-alert" role="alert">
                Successfully assigned trainer!
                <button class="btn" data-bs-dismiss="alert" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div`;
			} else {
				throw '';
			}
			initial_fetch();
		})
		.catch(() => {
			document.getElementById('insert-alert-div').innerHTML = `
        <div class=" container alert alert-danger alert-dismissible fade show" id="success-alert" role="alert">
            Failed assigning trainer!
            <button class="btn" data-bs-dismiss="alert" aria-label="Close">
                <span aria-hidden="true">&times;</span>
            </button>
        </div`;
		});
}
