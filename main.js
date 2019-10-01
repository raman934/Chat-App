console.log('Hello JS Buoy')

var socket = io();
socket.on('connect', function()
{
    socket.emit('my event', 
    	{
    		data: 'I\'m connected!'
    	});
});

function send()
{
	var inputBox = document.getElementById('inputBox')
	socket.emit('msg', inputBox.value)
	inputBox.value = ''
}

socket.on('push', function(data)
	{
		var msgBox = document.getElementById('msgBox')
		msgBox.innerHTML += '<p>' + data + '</p>'
		//console.log(data)
	})

function getWeather()
{
	//url='http://api.openweathermap.org/data/2.5/weather?q=Delhi&appid=03f31dc8f368ff2c95ed56faa28830f7'
	url='/users'
	fetch(url).then(function(res)
	{
		res.json().then(function(data)
		{
			console.log(data)
		})
	})
}