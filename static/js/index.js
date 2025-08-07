const BACKEND_URL = "http://127.0.0.1:5000"; // Replace with your actual IP when deploying

document
  .getElementById("student-form")
  .addEventListener("submit", async function (e) {
    e.preventDefault();

    const name = document.getElementById("name").value;
    const age = parseInt(document.getElementById("age").value);
    const marks = parseFloat(document.getElementById("marks").value);

    const response = await fetch(`${BACKEND_URL}/add_student`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ name, age, marks }),
    });

    if (response.ok) {
      document.getElementById("form-msg").textContent =
        "Student added successfully!";
      document.getElementById("student-form").reset();
      loadStudents();
    } else {
      document.getElementById("form-msg").textContent =
        "Failed to add student.";
    }
  });

async function loadStudents() {
  const res = await fetch(`${BACKEND_URL}/students`);
  const students = await res.json();
  const list = document.getElementById("student-list");
  list.innerHTML = "";

  students.forEach((student) => {
    const li = document.createElement("li");
    li.textContent = `${student.name} | Age: ${student.age} | Marks: ${student.marks} `;

  
    const deleteBtn = document.createElement("button");
    deleteBtn.textContent = "Delete";
    deleteBtn.style.marginLeft = "10px";
    deleteBtn.style.cursor = "pointer";
    deleteBtn.onclick = async () => {
      const res = await fetch(`${BACKEND_URL}/student/${student.id}`, {
        method: "DELETE",
      });

      if (res.ok) {
        // Remove item from DOM
        li.remove();
      } else {
        alert("Failed to delete student");
      }
    };

    li.appendChild(deleteBtn);
    list.appendChild(li);
  });
}
