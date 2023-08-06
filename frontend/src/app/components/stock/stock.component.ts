import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { StocksService } from 'src/app/services/stocks.service';
import { Stock } from 'src/app/models/stock';

@Component({
  selector: 'app-stock',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './stock.component.html',
  styleUrls: ['./stock.component.css']
})
export class StockComponent{

  stockList!: Stock[];

  constructor(private _stocksService: StocksService) {}

  showStocks(): void{
    this.stockList = this._stocksService.getStocks();
    // return this.stockList
  }

}
