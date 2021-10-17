let array1 = [1,2,3,9]
let sum = 8

for (let i =0; i < array1; i++) {
    for(let j = 0; j < array1; j++) {
        if (i + j === sum) {
            console.log(true)
        }
        else {
            console.log(false)
        }
    }

}
    
function HasPairWithSum(array1, sum) {
    let low = 0;
    let hi = array1.length - 1;
    while (low < hi) {
        let s = array1[low] + array1[hi];
        if (s === sum) {
            return true
        }
    }
};
