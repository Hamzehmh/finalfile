var dataset = null;
var originalDataset = null;
var tense = undefined;
var type = undefined;
var width = 0;


function hideInput() {
  if (dataset != null) {
    var input = document.getElementById("upload-container");
    input.style.display = "none";
  }
}

function getTenses() {
  if (dataset === null) return
  var unique = [...new Set(dataset.map(item => item.tense))];
  var select = document.getElementById("selectTense");
  for (var i = 0; i < unique.length; i++) {
    var opt = unique[i];
    var el = document.createElement("option");
    el.textContent = opt;
    el.value = opt;
    select.appendChild(el);
  }
}
function getTypes() {
  if (dataset === null) return
  var unique = [...new Set(dataset.map(item => item.type))];
  var select = document.getElementById("selectType");
  for (var i = 0; i < unique.length; i++) {
    var opt = unique[i];
    var el = document.createElement("option");
    el.textContent = opt;
    el.value = opt;
    select.appendChild(el);
  }

}


function filterDataSet() {
  dataset = originalDataset;
  if (dataset === null) return;

  if (tense !== undefined) {
    dataset = dataset.filter(obj => {
      return obj.tense === tense
    })
  }
  if (type !== undefined) {
    dataset = dataset.filter(obj => {
      return obj.type === type
    })
  }
}

function selectTense(input) {
  tense = input.value;
  filterDataSet()
}
function selectType(input) {
  type = input.value;
  filterDataSet()
}

function getData() {
  var item = dataset[Math.floor(Math.random() * dataset.length)];
  var question = document.getElementById("question");
  question.innerHTML = item["fa"]
  var answer = document.getElementById("answer");
  answer.innerHTML = item["en"]
  var tense = document.getElementById("tense");
  tense.innerHTML = "Tense : " + item["tense"]
  var type = document.getElementById("type");
  type.innerHTML = "Type : " + item["type"]
  removeFlip();
  progress_increment();
}

function getAnswer() {
  addFlip();
}

function addFlip() {
  var element = document.getElementById("answer-container");
  element.classList.add("add-flip");
}
function removeFlip() {
  var element = document.getElementById("answer-container");
  element.classList.remove("add-flip");
}

window.addEventListener('load', function () {
  var upload = document.getElementById('fileInput');

  // Make sure the DOM element exists
  if (upload) {
    upload.addEventListener('change', function () {
      // Make sure a file was selected
      if (upload.files.length > 0) {
        var reader = new FileReader(); // File reader to read the file 

        // This event listener will happen when the reader has read the file
        reader.addEventListener('load', function () {
          var result = JSON.parse(reader.result); // Parse the result into an object 
          originalDataset = result;
          dataset = result;
          hideInput();
          getData();
          getTenses();
          getTypes();
          removeFlip();
        });

        reader.readAsText(upload.files[0]); // Read the uploaded file
      }
    });
  }
});

function progress_increment() {
  let length = dataset.length;
  console.log(length % 100)
  var elem = document.getElementById("myBar");
  elem.style.display = "block"
  width++;
  elem.style.width = width + "%";
  if (width >= 100) {
    progress_reset();
  }
}

function progress_reset() {
  var elem = document.getElementById("myBar");
  width = 0;
  elem.style.display = "none"
  elem.style.width = width + "%";
} 
