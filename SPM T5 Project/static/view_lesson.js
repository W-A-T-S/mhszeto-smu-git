function update_material(checkbox) {
    const material_id = checkbox.value.split(",")[0]
    const lesson_id = checkbox.value.split(",")[1]
    const course_id = checkbox.value.split(",")[2]
    const learner_username = checkbox.value.split(",")[3]
    const class_id = checkbox.value.split(",")[4]
    if (checkbox.checked == true) {
        fetch(`/update_material_completed/${material_id}/${class_id}/${course_id}/${lesson_id}/${learner_username}`)
            .then((raw) => { window.location.reload(false); })

        return
    } else if (checkbox.checked == false) {
        fetch(`/update_material_incomplete/${material_id}/${class_id}/${course_id}/${lesson_id}/${learner_username}`)
            .then((raw) => { window.location.reload(false); })
            .catch((error) => {
                console.error('Error:', error);
            });

        return
    }
}