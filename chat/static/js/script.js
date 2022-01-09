resiver = none
function chat(sender_id,resiver_id){
    resiver = resiver_id
    console.log(sender_id,resiver_id)
    url = '/chat/'
    fetch(url,
    {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'sender':sender_id,'resiver':resiver_id})
    })
    .then((response)=>{
    console.log(response)
    response.json().then((data) => {
        make_chat(data)
    });
    })
}
function make_chat(data){

        right = document.getElementById('right')
        left = document.getElementById('left')
        text = "<div class='container' id='right'><img src='' alt='Avatar'><p>text</p><span class='time-right'>time</span></div>"
        messages = ''
        for(i=0;i<data.messages.length;i++){
            console.log(data.messages[i])
            if(data.messages[i].me){
                text = "<div class='container darker'><img src='" + data.messages[i].image + " 'alt='Avatar' class='right'><p>" + data.messages[i].text + "</p><span class='time-left'>" + data.messages[i].time + "</span></div>"
            }
            else{
                text = "<div class='container' id='right'><img src='" + data.messages[i].image + "' alt='Avatar'><p>" + data.messages[i].text + "</p><span class='time-right'>" + data.messages[i].time + "</span></div>"
            }
            messages += text
        }
        document.getElementById('chat').innerHTML = messages
}

function send_message(sender_id){
    console.log(sender_id, resiver)
    message = document.getElementById('message').value
    url = '/message/'
    fetch(url,
    {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'sender':sender_id,'resiver':resiver, 'message': message})
    })
    .then((response)=>{
    console.log(response)
    response.json().then((data) => {
        text = "<div class='container darker'><img src='" + data.image + " 'alt='Avatar' class='right'><p>" + data.message + "</p><span class='time-left'>"+ data.time +"</span></div>"
        document.getElementById('chat').innerHTML += text
    });
    })

}