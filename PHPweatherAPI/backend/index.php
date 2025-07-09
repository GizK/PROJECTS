/**
 * WEATHER API ENDPOINT
 * 
 * URL: /index.php?city={name}
 * Method: GET
 * 
 * Successful Response (200 OK):
 * {
 *   "city": "London",
 *   "temperature": 18.5,
 *   "condition": "Cloudy",
 *   "humidity": 65
 * }
 * 
 * Error Response (400 Bad Request):
 * {
 *   "error": "City not found"
 * }
 */




<?php
header("Content-Type: application/json");
header("Access-Control-Allow-Origin: *");

// Include config for API key
require_once "config.php";

// Get city from query parameter, default to London
$city = isset($_GET['city']) ? htmlspecialchars($_GET['city']) : 'London';
$apiKey = OPENWEATHER_API_KEY;

// Build OpenWeatherMap API URL
$apiUrl = "http://api.openweathermap.org/data/2.5/weather?q=$city&appid=$apiKey&units=metric";

// Initialize cURL session
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $apiUrl);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_TIMEOUT, 10);

// Execute cURL request
$response = curl_exec($ch);

// Check for errors


if (curl_errno($ch)) {
    http_response_code(500);
    echo json_encode(["error" => "Failed to fetch weather data: " . curl_error($ch)]);
    curl_close($ch);
    exit;
}
curl_close($ch);

// Decode and validate JSON response
$data = json_decode($response, true);
if (isset($data['cod']) && $data['cod'] != 200) {
    http_response_code($data['cod']);
    echo json_encode(["error" => $data['message'] ?? "Unknown error"]);
    exit;
}

// Return JSON response
echo json_encode([
    "city" => $data['name'],
    "temperature" => $data['main']['temp'],
    "condition" => $data['weather'][0]['description'],
    "humidity" => $data['main']['humidity'],
    "wind_speed" => $data['wind']['speed']
]);

// Manual test endpoint - Add to index.php - smoke and manual testing
if ($_GET['city'] === 'TESTCITY') {
    die(json_encode([
        "city" => "TESTCITY",
        "temperature" => 20,
        "condition" => "TESTING",
        "humidity" => 50
    ]));
}
