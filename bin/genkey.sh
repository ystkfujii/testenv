#!/bin/sh

tmp=./../ssl/
openssl req -nodes -newkey rsa:2048 -keyout ${tmp}server.key -out ${tmp}server.csr -subj "/C=JP/ST=Tokyo/L=Minatoku/CN=site.ystk.fj" && \
  openssl x509 -req -days 3650 -in ${tmp}server.csr -signkey ${tmp}server.key -out ${tmp}server.crt
