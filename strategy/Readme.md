# HW07
## 作業名稱:Quantopian策略建構

策略績效:
* Return = 105.05%
* Alpha = 0.09
* Beta = 1.01
* Sharpe = 0.89
* Drawdown = -44.31%

程式碼:

    def initialize(context):


      context.securities = [sid(22090), sid(17773), sid(1270),sid(24),sid(22073),
                            sid(25006)]

      schedule_function(rebalance, date_rule=date_rules.every_day())

    def rebalance(context, data):


      for stock in context.securities:


          price_history = data.history(
                                       stock,
                                       fields='price',
                                       bar_count=5,
                                       frequency='1d'
                                      )


          volume_history = data.history(
                                        stock,
                                        fields='volume',
                                        bar_count=1,
                                        frequency='1d'
                                        )


          average_price = price_history.mean()
          average_volume = volume_history.mean()


          current_price = data.current(stock, 'price')
          current_volume = data.current(stock, 'volume')


          if data.can_trade(stock):

              if current_price > (1.01 * average_price):
                  order_target_percent(stock, 1)
                  log.info("Buying %s" % (stock.symbol))

              elif current_price < average_price:
                  order_target_percent(stock, 0)
                  log.info("Selling %s" % (stock.symbol))

              if current_volume >  average_volume:
                  order_target_percent(stock, 1)
                  log.info("Buying %s" % (stock.symbol))

              elif current_volume < average_volume:
                  order_target_percent(stock, 0)
                  log.info("Selling %s" % (stock.symbol))


      record(current_price=current_price, average_price=average_price)
      record(current_volume=current_volume, average_volume=average_volume)
