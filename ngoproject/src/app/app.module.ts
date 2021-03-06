import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';

import { AppComponent } from './app.component';

import { HomeComponent } from './components/home/home.component';
import { DonationComponent } from './components/donation/donation.component';
import { RegisterComponent } from './components/register/register.component';
import { AmountComponent } from './components/amount/amount.component';

import { appRoutes } from './routerConfig';
import { SigninComponent } from './admin/signin/signin.component';
import { ChooseComponent } from './admin/choose/choose.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    DonationComponent,
    RegisterComponent,
    AmountComponent,
    SigninComponent,
    ChooseComponent
  ],
  imports: [
    BrowserModule, RouterModule.forRoot(appRoutes)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }