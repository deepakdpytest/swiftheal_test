//fixing the style of analyser
let container = document.getElementById("symptomanalyser_container");
let analyser = document.getElementById("symptomanalyser");
container.style.height = (window.innerHeight - container.offsetTop - 2) + "px";
if (container.getBoundingClientRect().height < 450) {
    container.style.height = "450px";
}
window.onload = function() {
    systemText("Hello!! Welcome to the symptom analyser");
    sendToServer({ "start": "start" });
}


const url = "/analyser/symptom";
let parameters = null; //parameters to send to server
let inputReady = false; //checks whether input is ready to send or not
let res = null; //response by the server
function systemText(message) {
    let node = document.createElement("div");
    node.classList.add("system");
    node.classList.add("text");
    node.innerText = message;
    analyser.appendChild(node);
}


function userText(message) {
    let node = document.createElement("div");
    node.classList.add("user");
    node.classList.add("text");
    node.innerHTML = message;
    analyser.appendChild(node);
}

function sendToServer(parameters) {
    let xhr = new XMLHttpRequest();
    xhr.open("POST", url);
    xhr.setRequestHeader("content-type", "application/json");
    xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
    //loading the loader animation if respose not ready
    xhr.onprogress = function() {
        let node = document.createElement("div");
        node.classList.add("loader");
        node.innerHTML = `<div class="info">Please Wait......</div>
        <div class="animation"><span></span><span></span><span></span><span></span><span></span></div>`
        analyser.appendChild(node);
    }
    xhr.onload = function() {
        analyser.removeChild(analyser.lastChild);
        parameters = null;
        inputReady = false;
        res = JSON.parse(this.response);

        //for response type to be message using system text to print message
        if (res['type'] == 'message') {
            systemText(res['question'])
            document.getElementById("send").innerText = "OK, I got it";
        }

        //for response type to be select
        else if (res['type'] == 'select') {
            select(res['question'], res['options'], res['multiple']);
        }

        //for response type to be range
        else if (res['type'] == 'range') {
            rangeselect(res['question'], res['max'], res['min']);
        }

        //for text input
        else if (res['type'] == 'text') {
            textInput(res['question']);
        }

        //for number input
        else if (res['type'] == 'number') {
            numberInput(res['question'], res['max'], res['min']);
        }

        //for picture select
        else if (res['type'] == 'picture') {
            picture(res['question'], res['options'], res['multiple']);
        }
        //for ending the question
        else if (res['type'] == 'end') {
            document.getElementById("send").style.display = "none";
            document.getElementById("abort").style.display = "block";
            systemText("Thanks for using the symptom analyser");
        } else {
            console.error('Some server error');
        }
    }
    parameters = JSON.stringify(parameters);
    xhr.send(parameters);
}

function select(question, options, multiple) {
    let node = document.createElement('div');
    node.classList.add("select");
    node.id = "activequestion";
    let systext = document.createElement('div');
    systext.classList.add('system');
    systext.classList.add('text');
    systext.innerText = question;
    node.appendChild(systext);
    let optionslst = document.createElement('ul');
    optionslst.classList.add('options');
    for (option of options) {
        let listitem = document.createElement('li');
        listitem.classList.add("option");
        listitem.innerText = option;
        optionslst.appendChild(listitem);
    }
    node.appendChild(optionslst);
    if (multiple) {
        clickmultiselect(optionslst);
    } else {
        clicksingleselect(optionslst);
    }
    analyser.appendChild(node);
}

function picture(question, options, multiple) {
    let node = document.createElement('div');
    node.classList.add("pictureSelect");
    node.id = "activequestion";
    let systext = document.createElement('div');
    systext.classList.add('system');
    systext.classList.add('text');
    systext.innerText = question;
    node.appendChild(systext);
    let optionslst = document.createElement('ul');
    optionslst.classList.add('options');
    for (option of options) {
        let listitem = document.createElement('li');
        listitem.classList.add("option");
        listitem.innerHTML = `<img src='${option}' alt='${option}' class='image'>`;
        optionslst.appendChild(listitem);
    }
    node.appendChild(optionslst);
    if (multiple) {
        clickmultiselect(optionslst);
    } else {
        clicksingleselect(optionslst);
    }
    analyser.appendChild(node);
}
document.getElementById('send').addEventListener("click", function() {
    if (getresponse()) {
        sendToServer(parameters);
        setTimeout(function() {
            analyser.scrollTop = analyser.scrollHeight;
            // analyser.scrollTo(0, analyser.getBoundingClientRect().height)
        }, 200);
    } else {
        window.alert("Enter valid response");
    }
})

function clickmultiselect(obj) {
    let options = Array.from(obj.children);
    options.forEach(elem => {
        elem.addEventListener("click", multiselect)
    })
}

function multiselect() {
    if (this.classList.contains('selected')) {
        this.classList.remove('selected');
    } else {
        this.classList.add('selected');
    }
}

function clicksingleselect(obj) {
    let options = Array.from(obj.children);
    options.forEach(elem => {
        elem.addEventListener("click", singleselect);

    })
}

function singleselect() {
    if (this.classList.contains('selected')) {
        this.classList.remove('selected');
    } else {
        let currselected = document.querySelector('#activequestion .selected');
        if (currselected == null) {
            this.classList.add('selected');
        } else {
            currselected.classList.remove('selected');
            this.classList.add('selected');
        }
    }
}

function rangeselect(question, max, min) {
    let node = document.createElement('div');
    node.classList.add("range-continous");
    let systext = document.createElement('div');
    systext.classList.add('system');
    systext.classList.add('text');
    systext.innerText = question;
    node.appendChild(systext);
    let wrapper = document.createElement('div');
    wrapper.classList.add('wrapper');
    wrapper.innerHTML = `<div class="min">${min}</div><div class="max">${max}</div><input id="activequestion" type="range" min=${min} max=${max} step="any">`;
    node.appendChild(wrapper);
    analyser.appendChild(node);
}

function textInput(question) {
    let node = document.createElement('div');
    node.classList.add("textInput");
    let systext = document.createElement('div');
    systext.classList.add('system');
    systext.classList.add('text');
    systext.innerText = question;
    node.appendChild(systext);
    let wrapper = document.createElement('div');
    wrapper.classList.add('textInput_wrapper');
    wrapper.innerHTML = `<textarea class='inputtext' id='activequestion'></textarea>`;
    node.appendChild(wrapper);
    let after = document.createElement('div');
    after.classList.add('textInputafter');
    analyser.appendChild(node);
}

function numberInput(question, max, min) {
    let node = document.createElement('div');
    node.classList.add("numberInput");
    let systext = document.createElement('div');
    systext.classList.add('system');
    systext.classList.add('text');
    systext.innerText = question;
    node.appendChild(systext);
    let wrapper = document.createElement('div');
    wrapper.classList.add('wrapper');
    wrapper.innerHTML = `<input type="number" id="activequestion" min=${min} max=${max}>`;
    node.appendChild(wrapper);
    let after = document.createElement('div');
    after.classList.add('numberInputafter');
    analyser.appendChild(node);
}

function getresponse() {
    if (res['type'] == 'message') {
        document.getElementById("send").innerText = "send";
        parameters = res;
        parameters['response'] = null;
        return true;
    } else if (res['type'] == 'select') {
        let options = document.querySelectorAll('#activequestion .selected');
        parameters = res;
        if (options.length == 0) {
            return false;
        }
        let message = "";
        response = [];
        for (i = 0; i < options.length; i++) {
            message += i + 1 + ') ' + options[i].innerText + `<br>`;
            response.push(options[i].innerText);
        }
        parameters['response'] = response;
        userText(message);
        let actquestion = document.getElementById("activequestion");
        options = Array.from(document.querySelectorAll("#activequestion .option"));
        if (res['multiple']) {
            options.forEach(elem => {
                elem.removeEventListener("click", multiselect);
            })
        } else {
            options.forEach(elem => {
                elem.removeEventListener("click", singleselect);
            })
        }
        actquestion.id = null;
        return true;
    } else if (res['type'] == 'range' || res['type'] == 'text' || res['type'] == 'number') {
        let inp = document.getElementById('activequestion');
        parameters = res;
        if (res['type'] == 'range') {
            userText(Math.round(inp.value));
        } else {
            userText(inp.value);
        }
        parameters['response'] = inp.value;
        inp.id = null;
        inp.setAttribute('disabled', true);
        return true;
    } else if (res['type'] == 'picture') {
        let options = document.querySelectorAll('#activequestion .selected');
        if (options.length == 0) {
            return false;
        }
        parameters = res;
        let arr = Array.from(document.querySelectorAll("#activequestion .selected img"));
        response = [];
        arr.forEach(elem => {
            response.push(elem.getAttribute('src'));
        })
        parameters['response'] = response;
        let actquestion = document.getElementById("activequestion");
        options = Array.from(document.querySelectorAll("#activequestion .option"));
        if (res['multiple']) {
            options.forEach(elem => {
                elem.removeEventListener("click", multiselect);
            })
        } else {
            options.forEach(elem => {
                elem.removeEventListener("click", singleselect);
            })
        }
        actquestion.id = null;
        return true;
    } else {
        return false;
    }
}

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}