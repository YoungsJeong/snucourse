import { NgModule } from '@angular/core';
import { SharedModule } from '../shared/shared.module';

import { IntroRoutingModule } from './intro-routing.module';
import { IntroComponent } from './intro/intro.component';
import { SigninComponent } from './signin/signin.component';

@NgModule({
  imports: [SharedModule, IntroRoutingModule],
  declarations: [IntroComponent, SigninComponent]
})
export class IntroModule {}
