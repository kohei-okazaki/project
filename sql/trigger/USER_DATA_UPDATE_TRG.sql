CREATE TRIGGER USER_DATA_UPDATE_TRG AFTER UPDATE 
  ON USER_DATA FOR EACH ROW 
INSERT 
INTO USER_DATA_HIST( 
  SEQ_USER_ID
  , PASSWORD
  , COMPANY_CD
  , REG_DATE
  , UPDATE_DATE
  , DIVISION_CD
  , DEL_FLG
) 
VALUES ( 
  NEW.SEQ_USER_ID
  , NEW.PASSWORD
  , NEW.COMPANY_CD
  , NEW.REG_DATE
  , NEW.UPDATE_DATE
  , NEW.DIVISION_CD
  , NEW.DEL_FLG
);