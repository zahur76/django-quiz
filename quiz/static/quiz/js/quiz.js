$(document).ready(function(){

    $(".logo").click(false);

    $(".next").hide();
    $(".correct_answer").hide();

    // Disable check button if no selection
    $(".check").attr("disabled", "disabled");
    $("input[type='radio']").change(function(){        
        $(".check").removeAttr("disabled");             
    });

    $(".check").click(function(){
        correctAnswer = $(".correct_answer").text();
        givenAnswer = $('input[name="answer"]:checked').val().split(".");
        console.log(givenAnswer)
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