const navElement = document.querySelector(".nav");
const hamburgerElement = document.querySelector(".hamburger");
const formSectionEl = document.querySelector(".main")
const signUpEl = document.querySelector(".singup")

hamburgerElement.addEventListener("click", () => {
    navElement.classList.toggle("nav--open");
    hamburgerElement.classList.toggle("hamburger--open");
    formSectionEl.classList.toggle('main-content')
    
});


document.addEventListener('DOMContentLoaded', function() {
    var fileInput = document.getElementById('fileInput');
    var fileSelectedSpan = document.getElementById('fileSelected');
    var analysisSelectedSpan = document.getElementById('analysisSelected');
    
    document.getElementById('openPopupBtn').onclick = function() {
        document.getElementById('popup').style.display = 'block';
    }
    
    document.getElementById('closePopupBtn').onclick = function() {
        document.getElementById('popup').style.display = 'none';
    }
    
    // document.getElementById('fileInput').onchange = function(event) {
    //     var file = event.target.files[0];
    
    //     if (file) {
    //         // Handle the file upload here. For demonstration, we'll just close the popup.
    //         alert("File " + file.name + " uploaded successfully.");
    
    //         // Close the popup
    //         document.getElementById('popup').style.display = 'none';
    //     }
    // }
    // Function to update the summary with file name
    function updateFileSummary() {
        var fileName = fileInput.files.length > 0 ? fileInput.files[0].name : 'None';
        fileSelectedSpan.textContent = fileName;
    }
    
        // Function to update the summary with selected analyses
        function updateAnalysisSummary() {
            var checkboxes = document.querySelectorAll('.analysis-checkbox');
            var selectedAnalyses = Array.from(checkboxes)
                                        .filter(checkbox => checkbox.checked)
                                        .map(checkbox => checkbox.value)
                                        .join(', ');
            selectedAnalyses = selectedAnalyses || 'None';
            analysisSelectedSpan.textContent = selectedAnalyses;
        }
    
        // Event listener for file selection
        fileInput.addEventListener('change', updateFileSummary);
    
        // Event listener for analysis checkbox changes
        document.querySelectorAll('.analysis-checkbox').forEach(function(checkbox) {
            checkbox.addEventListener('change', updateAnalysisSummary);
        });
    
        // Event listener for the form submission
    });
    
      // Feature File
      let currentIndex = 0;
const slides = document.querySelectorAll('.slide');
const totalSlides = slides.length;

function updateCarousel() {
    slides.forEach(slide => {
        slide.style.transform = `translateX(${-100 * currentIndex}%)`;
    });
}

function moveToNextSlide() {
    currentIndex = (currentIndex + 1) % totalSlides;
    updateCarousel();
}

document.querySelector('.prev').addEventListener('click', function() {
    currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
    updateCarousel();
});

document.querySelector('.next').addEventListener('click', function() {
    currentIndex = (currentIndex + 1) % totalSlides;
    updateCarousel();
});


setInterval(moveToNextSlide, 5000); 
