#!/usr/bin/env php

<?php
shell_exec("(sh -x ./load_urine.sh 2>&1 | tee -a file.log)");
?>