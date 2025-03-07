document.addEventListener('DOMContentLoaded', function () {
    const editButtons = document.getElementsByClassName("btn-edit");
    const commentText = document.getElementById("id_body");
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitButton");

    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteConfirm = document.getElementById("deleteConfirm");

    for (let button of editButtons) {
        button.addEventListener("click", (e) => {
            let commentId = e.target.getAttribute("data-comment-id");
            if (commentId) {
                let commentElement = document.getElementById(`comment${commentId}`);
                if (commentElement) {
                    let commentContent = commentElement.innerText;
                    commentText.value = commentContent;
                    submitButton.innerText = "Update";
                    commentForm.setAttribute("action", `/edit_comment/${commentId}/`);
                } else {
                    console.error(`Element with ID comment${commentId} not found`);
                }
            } else {
                console.error("Comment ID is null");
            }
        });
    }

    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let commentId = e.target.getAttribute("data-comment-id");
            if (commentId) {
                deleteConfirm.href = `/delete_comment/${commentId}/`;
                deleteModal.show();
            } else {
                console.error("Comment ID is null");
            }
        });
    }
});