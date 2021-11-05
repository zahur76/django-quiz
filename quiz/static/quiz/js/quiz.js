$(document).ready(function(){

    $(".logo").click(false);

    $(".next").hide();
    $(".correct_answer").hide();

    // Disable check button if no selection
    $(".check").attr("disabled", "disabled");
    $("input[type='radio']").change(function(){        
        $(".check").removeAttr("disabled");             
    });

    function getKeyByValue(object, value) {
        return Object.keys(object).find(key => object[key] === value);
      }

    correctAnswer = $(".correct_answer").text();
    
    $(".check").click(function(){
        correctAnswer = getKeyByValue(Data, correctAnswer);
        console.log(correctAnswer)
        givenAnswer = $('input[name="answer"]:checked').val().split(".");        
        if(correctAnswer==givenAnswer[0]){
            $(".result").html('Correct Answer!')
        }else{
            $(".result").html(`Incorrect, answer is ${correctAnswer}`)
        }
        $(".next").show();
        $(".check").hide();
        $("input[type='radio']").attr("disabled", "disabled");
    })
});