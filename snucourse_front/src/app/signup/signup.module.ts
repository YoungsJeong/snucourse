import { NgModule } from '@angular/core';

import { SignupRoutingModule } from './signup-routing.module';
import { SharedModule } from '../shared/shared.module';
import { SignupComponent } from './signup/signup.component';

@NgModule({
  imports: [SharedModule, SignupRoutingModule],
  declarations: [SignupComponent]
})
export class SignupModule {}
