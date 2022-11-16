let modal = document.getElementById("login-modal");
const formUrl = "login"
const forgetUrl = "ForgetUrl"

function openModal(type) {
    let label = document.querySelector("#login-modal #exampleModalLabel");
    if (type.toLowerCase() != 'patient') {
        document.getElementById("phoneselect").style.display = "none";
        document.querySelector("#aadharselect label").innerText = "User ID:"
    } else {
        document.getElementById("phoneselect").style.display = "block";
        document.querySelector("#aadharselect label").innerText = "Aadhar ID:"
    }
    label.innerText = "Welcome " + type;
    let link = formUrl + "/" + type.toLowerCase();
    let forgetlink = forgetUrl + type.toLowerCase();
    document.querySelector("#login-modal a").setAttribute("href", forgetlink);
    document.getElementById("loginForm").setAttribute('action', link);
    $("#login-modal").modal('show');
}

$("#phoneselect input").on("focus", function() {
    $("#phoneselect").css("opacity", 1);
    $("#phoneselect").attr("required", "true");
    $("#aadharselect input").val("");
    $("#aadharselect input").removeAttr("required")
    $("#aadharselect").css("opacity", 0.5);
})
$("#aadharselect input").on("focus", function() {
    $("#aadharselect").css("opacity", 1);
    $("#aadharselect").attr("required", "true");
    $("#phoneselect input").val("");
    $("#phoneselect").removeAttr("required");
    $("#phoneselect").css("opacity", 0.5);
})