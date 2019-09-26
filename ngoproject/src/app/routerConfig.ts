import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { DonationComponent } from './components/donation/donation.component';
import { RegisterComponent } from './components/register/register.component';
import { AmountComponent } from './components/amount/amount.component';
import { SigninComponent } from './admin/signin/signin.component';
import { ChooseComponent } from './admin/choose/choose.component';

export const appRoutes: Routes = [
  { path: '', 
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
  {
    path:'admin',
    component:SigninComponent
  },
  {
    path:'choose',
    component:ChooseComponent
  }

];