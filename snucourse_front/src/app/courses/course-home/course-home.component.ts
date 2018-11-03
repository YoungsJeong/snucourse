import { Component, OnInit } from '@angular/core';
import { LectureService } from '../../core/lecture.service';

@Component({
  selector: 'course-home',
  templateUrl: './course-home.component.html',
  styleUrls: ['./course-home.component.css']
})
export class CourseHomeComponent implements OnInit {
  pending: boolean;
  result = [];
  constructor(private lecture: LectureService) {}

  ngOnInit() {}

  search(payload) {
    this.pending = true;
    this.lecture.searchLectrue(payload).subscribe((result: any[]) => {
      this.pending = false;
      console.log(result);
      this.result = result;
    });
  }
}
