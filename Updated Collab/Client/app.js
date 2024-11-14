console.log("connected");

const apiUrl = window.location.protocol === 'file:'
  ? 'http://localhost:8080/rockclimbing' // Local API server during development
  : ''; // Production API

let ClimbingWrapper = document.querySelector("#climbing-review-wrapper");
let editRockClimbName = document.querySelector("#edit-climbing-name");
let editRockClimbDifficulty = document.querySelector("#edit-climbing-difficulty");
let editRockClimbColor = document.querySelector("#edit-climbing-color");
let editRockClimbHeight = document.querySelector("#edit-climbing-height");
let editRockClimbHold = document.querySelector("#edit-climbing-hold");
let editRockClimbRope = document.querySelector("#edit-climbing-rope");
let editRockClimbReview = document.querySelector("#edit-climbing-review");
let saveReviewButton = document.querySelector("#save-review-button");

let editID = null;

function saveReviewOnServer() {
        console.log("button clicked");
        //prep data to send to server
        let editData = "Name=" + encodeURIComponent(editRockClimbName.value);
        editData += "&Difficulty=" + encodeURIComponent(editRockClimbDifficulty.value);
        editData += "&Color=" + encodeURIComponent(editRockClimbColor.value);
        editData += "&Height=" + encodeURIComponent(editRockClimbHeight.value);
        editData += "&TypeofHold=" + encodeURIComponent(editRockClimbHold.value);
        editData += "&Rope=" + encodeURIComponent(editRockClimbRope.value);
        editData += "&Review=" + encodeURIComponent(editRockClimbReview.value);

        console.log("Edit data", editData)


    console.log("editdata" , editData)
    let method = "POST";
    let apiUrl
    if(editID){
        method = "PUT";
        URL = apiUrl +editID;
    }
    fetch(URL, {
        method: method,
        body: editData,
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        }
    }).then(function(response){
        console.log("New review created!", response)
        //ClimbingWrapper.textContent = "";
    })
}

function addRevieName(data){
    console.log("data", data)
    let rockclimbname = document.createElement("h3");
    rockclimbname.textContent = "Name: " + data.Name;
    let rockclimbcolor = document.createElement("h3");
    rockclimbcolor.textContent = "Color: " + data.Color;
    let rockclimbdifficulty = document.createElement("h3");
    rockclimbdifficulty.textContent = "Difficulty: " + data.Difficulty;
    let rockclimbheight = document.createElement("h3");
    rockclimbheight.textContent = "Height: " + data.Height;
    let rockclimbhold = document.createElement("h3");
    rockclimbhold.textContent = "Type of Hold : " + data.TypeofHold;
    let rockclimbrope = document.createElement("h3");
    rockclimbrope.textContent = "Rope?: " + data.Rope;
    let rockclimbreview = document.createElement("h3");
    rockclimbreview.textContent = "Review: " + data.Review;
    
    let editButton = document.createElement("button");
    editButton.textContent = "Edit";
    let climbSeparater = document.createElement("hr");
    ClimbingWrapper.appendChild(rockclimbname);
    ClimbingWrapper.appendChild(rockclimbdifficulty);
    ClimbingWrapper.appendChild(rockclimbcolor);
    ClimbingWrapper.appendChild(rockclimbheight);
    ClimbingWrapper.appendChild(rockclimbhold);
    ClimbingWrapper.appendChild(rockclimbrope);
    ClimbingWrapper.appendChild(rockclimbreview);
    ClimbingWrapper.appendChild(editButton);
    ClimbingWrapper.appendChild(climbSeparater);


    editButton.onclick = function () {
        console.log("climbing id: ", data.id)
        editRockClimbName.value = data.Name;
        editRockClimbDifficulty.value = data.Difficulty;
        editRockClimbColor.value = data.Color;
        editRockClimbHeight.value = data.Height;
        editRockClimbHold.value = data.TypeofHold;
        editRockClimbRope.value = data.Rope;
        editRockClimbReview.value = data.Review;
        editID = data.id
    }
}

function loadReviewFromServerName() {
    fetch(apiUrl)
    .then(function(response2){
        response2.json()
            .then(function(data){
                console.log(data);
                let stadiumReviews = data;
                stadiumReviews.forEach(addRevieName)

           })
    })
}

let addReviewButton = document.querySelector("#add-review-button");
function addNewReview(){
    console.log("button clicked");
    let inputReview = document.querySelector("#add-review-button");
    console.log(inputReview.value);
    //prep data to send to server
    let editData = "Name=" + encodeURIComponent(editRockClimbName.value);
    editData += "&Difficulty=" + encodeURIComponent(editRockClimbDifficulty.value);
    editData += "&Color=" + encodeURIComponent(editRockClimbColor.value);
    editData += "&Height=" + encodeURIComponent(editRockClimbHeight.value);
    editData += "&TypeofHold=" + encodeURIComponent(editRockClimbHold.value);
    editData += "&Rope=" + encodeURIComponent(editRockClimbRope.value);
    editData += "&Review=" + encodeURIComponent(editRockClimbReview.value);
    fetch(apiUrl, {
            method: "POST",
            body: editData,
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            }
    }).then(function(response){
        console.log("New review created!", response)
        ClimbingWrapper.textContent = "";
        loadReviewFromServerName()
    })
}



addReviewButton.onclick = addNewReview;
saveReviewButton.onclick = saveReviewOnServer;

loadReviewFromServerName()