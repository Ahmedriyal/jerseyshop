var updateBtns = document.getElementsByClassName('update-cart')

for (var i=0; i<updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var jerseyId = this.dataset.jersey
        var action = this.dataset.action
        console.log('jerseyId:', jerseyId, 'action:', action)

        console.log('USER:', user)
        if(user == 'AnonymousUser'){
            console.log('Not logged in')
        }
        else{
            updateUserOrder(jerseyId, action)
        }
    })
}

function updateUserOrder(jerseyId, action){
    console.log('User is logged in, sending data..')

    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'jerseyId': jerseyId, 'action': action})
    })
    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data:', data)
        location.reload()
    })
}