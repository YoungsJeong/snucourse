import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../core/auth.service';

@Component({
  selector: 'profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  graduate;
  progress = 0;
  constructor(public auth: AuthService) {}

  ngOnInit() {
    this.auth.getGraduateAssessment().subscribe(graduate => {
      this.graduate = graduate;
      this.progress = Math.floor(
        graduate.took_total_credit /
          (graduate.total_credit_need + graduate.took_total_credit) *
          100
      );
    });
  }
}
