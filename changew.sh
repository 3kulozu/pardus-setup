resim=$1
#resim="/tmp/w.jpg"

xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/image-path -n -t string -s  $resim
xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitorLVDS1/workspace0/last-image -n -t string -s  $resim

for i in $(xfconf-query -c xfce4-desktop -p /backdrop -l|egrep -e "screen.*/monitor.*image-path$" -e "screen.*/monitor.*/last-image$"); do
    echo "$i"
    xfconf-query -c xfce4-desktop -p $i -n -t string -s $resim
    xfconf-query -c xfce4-desktop -p $i -s $resim

done
