


var animal = {};
var animal_name = "";
var animal_list = [];

var win = 0;    
var guess = 0;
var hintNum = 0;
var canClick = true

var hints = [];
var currAnimal = [];

var currSolution = "";
var answer = "";

var again = document.createElement("Button");
var button = document.getElementById("guessButton");


fetch("genus_data.csv")
    .then(response => response.text())
    .then(csv => {
        
        const rows = csv.trim().split("\n");
        var data = rows.map(row => row.split(","));

        const size = rows.length;
        const randomNum = Math.floor(Math.random() * size);

        const key = data[0].splice(1);

        data = data.splice(1);
        var data2 = data[randomNum];


        animal_name = data2[0];
        data2 = data2.splice(1);
        
        const dict = Object.fromEntries(
            key.map((key, i) => [key, data2[i]])
        );
        animal = dict;

        console.log(dict)
        console.log(animal_name);
        animal_list = data2;

        hints.push(["Order", "What Class of Animal is it?"]);
        hints.push(["Weight (kg)", "How Much Does an Adult Weigh?"]);
        hints.push(["Color", "What Color is it?"]);
        hints.push(["Lifespan (years)", "What is their Average Lifespan?"]);
        hints.push(["Diet", "What is their Diet?"]);
        hints.push(["Habitat", "What Biome Does it Live in?"]);
        hints.push(["Conservation Status", "What is their Conservation Status"]);
        hints.push(["Social Structure", "What is their Social Structure"]);

        hints = hints.reverse();

        currAnimal = [animal_name, animal]

        console.log(currAnimal);

        for (let hintNum = 0; hintNum < hints.length; hintNum++) {
            hints[hintNum][2] = currAnimal[hints[hintNum][0]];
            
        }
        hints.push(["Location", "Where does it Live?", "range_images/" + animal_name + "_range.png"])

        console.log(hints)

        
        again.id = "again";        
        again.innerHTML = "Play Again";
        again.onclick = function reload() {
            location.reload();
        };    


        var pickOption = document.createElement("p");    
        pickOption.innerHTML = "Pick one the the following options:";
        document.body.append(pickOption);

        var allBox = document.createElement("div");
        allBox.classList.add("boxContainer");

        for (var box = 1; box <= 4; box++) {
            allBox = createBox(allBox);
        }   
        document.body.appendChild(allBox);

        currSolution = animal_name;
        currAnimalInfo = currAnimal[1];
        answer = (document.getElementById("currGuess")).value;


   });

    function checkAnswer() {

        guess = guess + 1;
        answer = (document.getElementById("currGuess")).value;

        var currGuess = document.getElementById("currGuess");
        currGuess.value = "";

        if (answer.toUpperCase() == currSolution.toUpperCase()) {
            win = 1;
            currGuess.classList.add('success-placeholder');
            currGuess.placeholder = answer;
            alert("You Won in " + String(guess) + " guesses and with " + String(hintNum) + " hints.");
            start.appendChild(again);


        } else {
            
            currGuess.classList.add('failure-placeholder');
            currGuess.placeholder = answer;
            
                
        }
        button.remove();



        if (hints.length <= 0) {
            alert("You Lose. Correct Answer: " + currSolution + ".");
            start.appendChild(again);
        }
            
    }


    function createBox(allBox) {
                
        var newBox = document.createElement("button");
        newBox.classList.add("infoBox");
        var questions = hints.pop();
        newBox.id = questions[0];
        newBox.innerHTML = questions[1];

        newBox.onclick = function() {
            this.disabled = true
            hintNum = hintNum + 1;
            this.style.marginBottom = "100px";

            function removeFunc() {
                newBox.remove();
                        
                if (questions[0] != "Location") {
                    var newInfo = document.createElement("p");
                    newInfo.classList.add("answer");
                    newInfo.innerHTML = currAnimalInfo[questions[0]];
                    document.body.appendChild(newInfo);
                } else {
                    var newImage = document.createElement("img");
                    newImage.style.display = "block";
                    newImage.style.marginLeft = "auto";
                    newImage.style.marginRight = "auto";

                    newImage.src = questions[2];
                    newImage.alt = "????";
                    newImage.width = 250;
                    newImage.height = 200;
                    document.body.appendChild(newImage);
                    var newInfo = document.createElement("p");
                }
                        
                if (hints.length > 0) {
                    createBox(allBox);  
                }


                if (win == 0) {                    
                    start.appendChild(button);
                }   
            }
            setTimeout(removeFunc, 800);
                
                    
        }

        allBox.appendChild(newBox);
        return allBox;
    }
        
 



