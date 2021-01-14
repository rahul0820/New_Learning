
// IF Statement
// var hot = false
// var temp = 90

// if (temp>80) {
//     hot=true
// }
// console.log(hot);

// IF ELSE Statement

// var hot = false
// var temp = 60
// if (temp>60) {
//     console.log("Hot outside");
    
// } else {
//     console.log("it's normal");
    
// }

//ELSE IF Statement
// var hot =false
// var temp = 24

// if (temp>60) {
//     console.log("Hot Outside");
    
// } else if (temp<=60 && temp>=35) {
//     console.log("Normal Outside");

    
// } else if(temp<=35 && temp>=25) {
//     console.log("it's cold");
// }else{
//     console.log("very cold");
// }

//Other examaples with comparator
var bat=10
var ball=10

var report ="blank"

if (bat>=10 && ball>=10) {
    report = "Great sale"
    
}else if (bat ===0 && ball === 0){

    report ="Zero Sale"
}else if (bat===0 && ball <=10){
    report="bat zero sale but some balls sold"
}else{
    report="someting sold"
}
console.log(report);