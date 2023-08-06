import { Injectable } from '@angular/core';
import { STOCKLIST } from '../components/stock/stocklist';
import { Stock } from '../models/stock';

@Injectable({
  providedIn: 'root'
})
export class StocksService {

  constructor() { }

  getStocks(): Stock[] {
    return STOCKLIST;
  }
}
