#!/bin/bash

sed -n '/`/,$p' prueba.txt | sed -n '/^\([^`]*`\)\{6\}/q;p' > buena

tail -n +2 buena | head -n $(($(wc -l < buena) - 3)) > arqui.json
