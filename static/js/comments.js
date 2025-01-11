const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_comment_field");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        let commentContent = document.getElementById(
          `comment${commentId}`).innerText;
        commentText.value = commentContent;
        submitButton.innerText = "Update";
        commentForm.setAttribute("action", `comment_edit/${commentId}/`);
    });
}