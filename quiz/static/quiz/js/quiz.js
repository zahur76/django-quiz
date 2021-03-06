$(document).ready(function(){

    $(".logo").click(false);

    $(".next").hide();
    $(".correct_answer").hide();
    $('.path').hide()
    $('.path-two').hide()

    // Disable check button if no selection
    $(".check").attr("disabled", "disabled");
    $("input[type='radio']").change(function(){        
        $(".check").removeAttr("disabled");             
    });

    function getKeyByValue(object, value) {
        return Object.keys(object).find(key => object[key] === value);
    }    
    correctAnswer = $(".correct_answer").text();

    let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    let url = '/quiz/save_answer';   
    let path = $('.path').html();
    let pathTwo = $('.path-two').html();

    let endDigit = parseInt(pathTwo.slice(-1)) + 1  
    $(".check").click(function(){                                
        correctAnswer = getKeyByValue(Data, correctAnswer);        
        givenAnswer = $('input[name="answer"]:checked').val().split(".");        
        if(correctAnswer==givenAnswer[0]){
            $(".result").html('Correct Answer!')
            console.log(url)
            $.post(url, {csrfmiddlewaretoken: csrfToken, "answer": "correct", "id": Data.id}).done(function(response){                                   
                console.log(response)
                if(response=='False' & endDigit<Data['length']){
                    $(".result").html('Question already answered!')                  
                    setInterval(() => {
                        window.location.replace(path);
                    }, 2000);   
                }                
            });            
        }else{
            $(".result").html(`Incorrect, answer is ${correctAnswer}`)
            $.post(url, {csrfmiddlewaretoken: csrfToken, "answer": "incorrect", "id": Data.id}).done(function(response){                                   
                console.log(response)
                if(response=='False' & endDigit<Data['length']){
                    $(".result").html('Question already answered!')
                    setInterval(() => {
                        window.location.replace(path);
                    }, 2000);                   
                }  
            });
        }
        $(".next").show();
        $(".check").hide();
        $("input[type='radio']").attr("disabled", "disabled");
    })
});