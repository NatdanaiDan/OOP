function add_list() {
    let list_name = document.getElementById("list_name").value
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            console.log("add successfully")
        }
    };
    xmlhttp.open("GET", "http://127.0.0.1:8000/addlist?name=" + list_name, true);
    xmlhttp.send();
}

function get_data() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let result = JSON.parse(this.responseText);
            let todo_dom = document.getElementById("todo_app");
            todo_dom.innerHTML = result
        }
    };
    xmlhttp.open("GET", "http://127.0.0.1:8000/get_data", true);
    xmlhttp.send();
}