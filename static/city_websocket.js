var city_selector = document.getElementById('id_city'),
	city_temp = document.getElementById('city_temp'),
	city_desc = document.getElementById('city_desc'),
	city_icon = document.getElementById('city_icon')

function get_socket(ws_url){
	const socket = new ReconnectingWebSocket(
		'ws://'
		+ window.location.host
		+ ws_url
	);
	socket.debug = false;
	socket.timeoutInterval = 1000000;
	socket.reconnectInterval = 1000;
	return socket
}

function set_weather(data){
	city_temp.innerText = data.temperature
	city_desc.innerText = data.description
	city_icon.setAttribute('src', 'http://openweathermap.org/img/wn/' +  data.icon +'@2x.png')
}

function set_socket(city_id){
	CITY_SOCKET = get_socket('/ws/city/' + city_id + '/')

	CITY_SOCKET.onmessage = function(e) {
		const data = JSON.parse(e.data);
		set_weather(data)
	};
	CITY_SOCKET.onclose = function(e) {
		console.error('Connection Close');
	};
	CITY_SOCKET.onopen = function(e) {
		// console.log('Open');
	};
	CITY_SOCKET.onerror = function(e) {
		console.log(e);
	};
}

city_selector.onchange = ()=>{
	let city_id = city_selector.value
	set_socket(city_id)
}

set_socket(city_selector.value)

