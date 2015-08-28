<?php

$x = 0;

while($x < 3) {

	$nagiosData = file_get_contents('http://nagiosjson.elucas.dev/statusJson.php');
	$dataArray = json_decode($nagiosData, true);

	$hosts = $dataArray['hosts'];
	$services = $dataArray['services'];

	$downHosts = 0;
	$criticalServices = 0;

	foreach($hosts as $hostname) {
		if($hostname['current_state'] == '1') {
			$downHosts++;
		}
	}

	foreach($services as $servicename) {
		foreach($servicename as $name => $type) {
			if($type['current_state'] == '2') {
				$criticalServices++;
			}
		}
	}

	file_put_contents('/tmp/downhosts.tmp', $downHosts);
	file_put_contents('/tmp/criticalservices.tmp', $criticalServices);

	sleep(19);

	$x++;
}
