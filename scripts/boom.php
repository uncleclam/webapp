#!/usr/bin/env php

<?php
shell_exec("./s3_load.sh");

header('Location: http://18.219.109.83/done.html');

exit;

?>
