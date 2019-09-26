import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { DonationComponent } from './components/donation/donation.component';
import { RegisterComponent } from './components/register/register.component';
import { AmountComponent } from './components/amount/amount.component';


export const routes: Routes = [
  { path: 'home', 
    component: HomeComponent 
  },
  {
    path: 'donation',
    component: DonationComponent
  },
  { path: 'register',
    component: RegisterComponent
  },
  { path: 'amount',
    component: AmountComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

