import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { DonationComponent } from './components/donation/donation.component';
import { RegisterComponent } from './components/register/register.component';
import { AmountComponent } from './components/amount/amount.component';
import { SigninComponent } from './admin/signin/signin.component';
import { ChooseComponent } from './admin/choose/choose.component';


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
  },
  { path: 'signin',
    component: SigninComponent
  },

  {
    path:'choose',
    component:ChooseComponent
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

