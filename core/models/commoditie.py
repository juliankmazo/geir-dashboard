from core.models import BaseModel


class Commoditie(BaseModel):

    @classmethod
    def populate(cls):
        for c in cls.COMMODITIES:
            commoditie = Commoditie.query(Commoditie.code == c[0]).get()
            if not commoditie:
                new_commoditie = Commoditie(code=c[0], column=c[1])
                new_commoditie.put()

    COMMODITIES = [['CHRIS/ICE_T1', 1],         # WTI Crude Oil Price
                   ['OFDP/FUTURE_C1', 1],       # Corn
                   ['OFDP/FUTURE_SB1', 1],      # Sugar
                   ['OFDP/COPPER_6', 1],        # Copper
                   ['YAHOO/TSX_XGD_TO', 1],     # Gold
                   ['OFDP/FUTURE_B1', 1],       # Brent Crude
                   ['OFDP/FUTURE_W1', 1],       # Wheat
                   ['OFDP/FUTURE_KC1', 1],      # Coffee
                   ['OFDP/ALUMINIUM_21', 1],    # Aluminium
                   ['LBMA/SILVER', 1],          # Silver
                   ['CHRIS/CME_NG1', 1],        # Natural Gas
                   ['OFDP/FUTURE_S1', 1],       # Soybean
                   ['OFDP/FUTURE_CT1', 1],      # Cutton
                   ['OFDP/NICKEL_41', 1],       # Nickel
                   ['JOHNMATT/PLAT', 1],        # Platinum
                   ['OFDP/FUTURE_RB1', 1],      # Gasoline
                   ['OFDP/FUTURE_RR1', 1],      # Rice
                   ['OFDP/FUTURE_CC1', 1],      # Cocoa
                   ['OFDP/STEELBILLET_46', 1],  # Steel
                   ['JOHNMATT/PALL', 1]         # Palladium
                   ]
