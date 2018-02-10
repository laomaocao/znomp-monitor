while true
do
time=`date +"%D %T"`
price=`curl -s https://api.coinmarketcap.com/v1/ticker/zcash/ | jq '.[]["price_usd"]' | tr -d '"'`
nethash=`zcash-cli getnetworkhashps`
echo $time $price $nethash
sleep 300
done

