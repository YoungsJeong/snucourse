import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../core/auth.service';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'graduate-home',
  templateUrl: './graduate-home.component.html',
  styleUrls: ['./graduate-home.component.css']
})
export class GraduateHomeComponent implements OnInit {
  graduate;
  lowerGrade;
  constructor(private auth: AuthService, private modal: NgbModal) {}

  openModal(content) {
    this.modal.open(content, { size: 'lg' });
  }
  ngOnInit() {
    this.auth.getGraduateAssessment().subscribe(graduate => {
      this.graduate = graduate;
      this.lowerGrade = this.filterLowerGrade(graduate.majors);
    });
  }

  filterLowerGrade(courses: any[]) {
    const grade = 2018 - Math.floor(this.auth.user.student_id / 100000) + 1;
    return courses.filter(
      (course: any) => Number.parseInt(course.grade[0]) < grade
    );
  }
}
