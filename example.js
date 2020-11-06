function foo(){
    console.log("Foo")
}

function bar(){
    console.log("Bar")
}

for(var i=0; i<10; i++){
    if(i%2===0){
        foo();
    } else{
        bar();
    }
}

console.log("done")