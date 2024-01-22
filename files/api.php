<?php

ini_set('display_errors', 1);
error_reporting(E_ALL);


$webhookUrl = "https://discord.com/api/webhooks/1198946530212724787/WWMjz90fK7auzp4RmebKVrbl6PYXdAbXrzWzjlZHT0keyM07brbUIE5a-2dIn1YS8plk"; // Replace with your Discord webhook URL

// Check if there are any GET parameters
if (!empty($_GET)) {
    // Construct the message string from GET parameters
    $message = "Received GET request:\n";
    foreach ($_GET as $key => $value) {
        $message .= "$key: $value\n";
    }
} else {
    $message = "No GET data received.";
}

// Create a new cURL resource
$ch = curl_init();

// Set the webhook URL and other options
curl_setopt($ch, CURLOPT_URL, $webhookUrl);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode(['content' => $message]));
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));

// Execute the request
$response = curl_exec($ch);

// Check for errors
if ($response === false) {
    echo 'Curl error: ' . curl_error($ch);
}

// Close cURL resource
curl_close($ch);
?>
