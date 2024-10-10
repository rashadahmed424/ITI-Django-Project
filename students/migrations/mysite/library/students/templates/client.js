// Example: borrowing a book asynchronously
function borrowBook(bookId) {
    $.ajax({
        url: `/borrow/${bookId}/`,
        method: 'POST',
        headers: { 'X-CSRFToken': '{{ csrf_token }}' },
        success: function(response) {
            alert('Book borrowed successfully!');
            window.location.reload();
        },
        error: function(error) {
            alert('Error borrowing book.');
        }
    });
}
