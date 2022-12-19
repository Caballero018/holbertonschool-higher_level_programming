#!/usr/bin/node
const args = process.argv;
const len = Object.keys(args).length;

function findSecondLargestElem(arr){
    let first = -1 , second = -1;

    for(let i = 0; i <= Object.keys(arr).length -1; i++){
        if(arr[i] > first){
            second = first;
            first = arr[i];
        }
        else if(arr[i] > second && arr[i] != first){
            second = arr[i];
        }
    }
    console.log(second);
}

if (len > 3) {
  findSecondLargestElem(args);
} else {
  console.log(1);
}
