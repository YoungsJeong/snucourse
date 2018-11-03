import { Component, OnInit, Input, OnChanges } from '@angular/core';
import { LectureService } from '../../core/lecture.service';

@Component({
  selector: 'course-detail',
  templateUrl: './course-detail.component.html',
  styleUrls: ['./course-detail.component.css']
})
export class CourseDetailComponent implements OnInit, OnChanges {
  @Input() course: string;
  lecture;
  content;
  credit = 0;
  easy = 0;
  useful = 0;
  Math = Math;
  invalid: boolean;
  constructor(public lectureService: LectureService) {}

  ngOnInit() {}

  ngOnChanges() {
    this.lectureService.getLectureDetail(this.course).subscribe(lecture => {
      this.lecture = lecture;
      console.log('lecture: ', lecture);
    });
  }

  get avg() {
    return Math.floor((this.credit + this.easy + this.useful) / 3);
  }

  writeOpinion() {
    if (!this.content || this.content.trim() === '') {
      this.invalid = true;
    } else {
      this.lectureService
        .writeOpinion({
          content: this.content,
          lecture: this.lecture.id,
          easy: this.easy,
          useful: this.useful,
          credit: this.credit
        })
        .subscribe(opinion => {
          this.content = '';
          this.lectureService.alreadyReviewed.push(this.lecture.id);
          this.lecture.lectureopinion_set.push(opinion);
          this.lectureService
            .getLectureDetail(this.course)
            .subscribe(lecture => {
              this.lecture = lecture;
            });
        });
    }
  }

  alreadyReviewed() {
    return this.lectureService.alreadyReviewed.includes(
      this.lecture && this.lecture.id
    );
  }
}
