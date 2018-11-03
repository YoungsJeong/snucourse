import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../../core/auth.service';
import { FormGroup, FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'signin',
  templateUrl: './signin.component.html',
  styleUrls: ['./signin.component.css']
})
export class SigninComponent implements OnInit {
  pending: boolean;
  error: any;
  submitAttempt: boolean;
  signInForm: FormGroup;
  constructor(private router: Router, private auth: AuthService) {}

  ngOnInit() {
    this.createForm();
  }

  createForm() {
    this.signInForm = new FormGroup(
      {
        email: new FormControl(
          '',
          Validators.compose([Validators.email, Validators.required])
        ),
        password: new FormControl('', Validators.required)
      },
      { updateOn: 'submit' }
    );
  }

  goToSignUp() {
    console.log();
    this.router.navigate(['/signup']);
  }

  login() {
    this.submitAttempt = true;
    if (this.signInForm.valid) {
      this.pending = true;
      this.error = false;
      this.auth.login(this.formEmail.value, this.formPassword.value).subscribe({
        error: err => {
          console.error('signin error: ', err);
          this.pending = false;
          this.error = true;
        },
        complete: () => {
          this.pending = false;
        }
      });
    }
  }

  get formEmail() {
    return this.signInForm.get('email');
  }

  get formPassword() {
    return this.signInForm.get('password');
  }
}
