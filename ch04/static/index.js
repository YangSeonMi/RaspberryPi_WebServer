var todos = document.querySelector('#todos')

todos.addEventListener('click', function(){
    $.ajax({
        type: 'GET',
        url: 'https://jsonplaceholder.typicode.com/todos',
        dataType: 'json'
    }).done(function(result) {
        console.log(result)
        var tableData=""
        for(var i in result) {
            var obj = result[i]
            console.log(obj.title)
            tableData += "<tr>"
            tableData += "<td>"+obj.userId+"</td>"
            tableData += "<td>"+obj.title+"</td>"
            tableData += "<td>"+obj.completed+"</td>"
            tableData += "</tr>"
        }
        document.querySelector("#data").innerHTML += tableData
    }).fail(function(result) {
        console.log(result)
    })
  });
