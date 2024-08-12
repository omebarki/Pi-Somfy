#!/bin/bash

cd /home/omar/code_workspace/Pi-Somfy/
cp /home/omar/code_workspace/Pi-Somfy/garage.service /etc/systemd/system/garage.service

systemctl daemon-reload
systemctl enable garage
systemctl start garage
