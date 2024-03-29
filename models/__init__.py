from pydantic import BaseModel
#from typing import Optional


class input_data_model(BaseModel):
    timeframe: str
    financial_instrument_name: str
    #provider: str


class backtest_strategy_model(BaseModel):
    start_date: str
    end_date: str
    input_data: input_data_model
    initial_portfolio_value: float
    indicators_parameters: dict
    risk_free_rate: float
